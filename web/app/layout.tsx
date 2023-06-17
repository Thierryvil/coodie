import Provider from "./components/Provider";
import { Roboto } from "next/font/google";

const roboto = Roboto({ subsets: ["latin"], weight: "300" });

export const metadata = {
  title: "coodie",
};

interface Props {
  children: React.ReactNode;
}

export default function RootLayout({ children }: Props) {
  return (
    <html lang="en">
      <Provider>
        <body className={roboto.className}>{children}</body>
      </Provider>
    </html>
  );
}
