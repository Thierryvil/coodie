import NextAuth from "next-auth";

declare module "next-auth" {
  interface Session {
    user?: {
      name?: string | null | undefined;
      email?: string | null | undefined;
      image?: string | null | undefined;
      access_token?: string | null | undefined;
    };
  }
}
