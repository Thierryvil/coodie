import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import { COODIE_API_URL } from "../../../app/constants";

export default NextAuth({
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        email: {},
        password: {},
      },
      async authorize(credentials, req) {
        const data = {
          username: credentials?.email ?? "",
          password: credentials?.password ?? "",
        };

        console.log(`COODIE LOG == ${data}`);

        const res = await fetch(`${COODIE_API_URL}/auth/token`, {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          body: new URLSearchParams(data),
        });
        console.log(`COODIE LOG == ${res.json()}`);

        if (!res.ok) {
          throw new Error("Invalid credentials");
        }

        const user = await res.json();
        if (user) {
          return user;
        } else {
          return null;
        }
      },
    }),
  ],
  callbacks: {
    async jwt({ token, user }) {
      return { ...token, ...user };
    },
    async session({ session, token, user }) {
      session.user = token as any;
      return session;
    },
  },
});
