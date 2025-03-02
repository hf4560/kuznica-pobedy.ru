import { useEffect } from "react";
import { Outlet } from "react-router-dom";
import Header from "./Header";

const Layout = () => {
  useEffect(() => {
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = "";
    };
  }, []);

  return (
    <div className="h-screen flex flex-col">
      <Header />
      <main className="w-full h-[calc(100vh-5rem)] overflow-hidden">
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;
