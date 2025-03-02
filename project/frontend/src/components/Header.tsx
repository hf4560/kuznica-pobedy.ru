import { Link, useLocation } from "react-router-dom";
import logo from "../assets/logo.png";
import { useState, useEffect } from "react";
import axios from "axios";

const Header = () => {
  const location = useLocation();
  const [links, setLinks] = useState<any[]>([]);

  useEffect(() => {
    // Запрашиваем ссылки с бэкенда
    axios
      .get("http://localhost:8000/api/headerlinks")
      .then((response) => {
        setLinks(response.data);
      })
      .catch((error) => {
        console.error("Error fetching header links:", error);
      });
  }, []);

  return (
    <header className="w-full bg-stone-200 text-gray-950">
      <div className="p-4 flex justify-between items-center max-w-screen-xl mx-auto">
        <nav className="flex items-center space-x-6">
          <Link to="/" className="flex items-center">
            <img
              src={logo}
              alt="ЛОГО"
              className="h-15 w-auto"
            />
          </Link>

          {/* Маппим ссылки на основе данных с бэкенда */}
          {links.map((link) => (
            <Link
              key={link.link_to}
              to={link.link_to}
              className={`text-lg hover:text-slate-800 transition-colors ${
                location.pathname === link.link_to ? "text-rose-950" : ""
              }`}
            >
              {link.text}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
};

export default Header;
