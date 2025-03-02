import { Link, useLocation } from "react-router-dom";
import logo from "../assets/logo.png";
import { useState, useEffect, useRef } from "react";
import axios from "axios";

const Header = () => {
  const location = useLocation();
  const [links, setLinks] = useState([]);
  const [isHovered, setIsHovered] = useState(null); // Хранение состояния наведения
  const navRef = useRef(null);
  const linkRefs = useRef(new Map());

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/headerlinks")
      .then((response) => {
        const sortedLinks = response.data.sort((a, b) => a.id - b.id);
        setLinks(sortedLinks);
      })
      .catch(() => {});
  }, []);

  const renderSubmenu = (submenu) => {
    return submenu.length > 0 && (
      <div className="absolute top-full left-1/2 transform -translate-x-1/2 p-4 bg-white shadow-lg w-max h-auto overflow-auto">
        <ul className="space-y-2">
          {submenu.map((subLink) => (
            <li key={subLink.id}>
              <Link
                to={subLink.link_to}
                className="text-sm md:text-lg lg:text-xl xl:text-2xl hover:text-slate-800 block py-2 px-4"
              >
                {subLink.text}
              </Link>
            </li>
          ))}
        </ul>
      </div>
    );
  };

  return (
    <header className="w-full h-20 flex bg-stone-200 items-center text-gray-950">
      <Link to="/" className="flex items-center">
        <img src={logo} alt="ЛОГО" className="h-auto w-20 ml-5 p-2" />
      </Link>
      <div className="p-2 flex justify-center items-center max-w-screen-xl mx-auto w-full">
        <nav className="flex flex-wrap justify-center items-center mx-auto h-20 w-full">
          {links.map((link) => (
            <div
              key={link.link_to || link.id}
              className="relative flex-grow flex justify-center items-center"
              onMouseEnter={() => setIsHovered(link.id)}  // Навели на элемент меню
              onMouseLeave={() => setIsHovered(null)}    // Ушли с элемента меню
            >
              {link.link_to ? (
                <Link
                  to={link.link_to}
                  ref={(el) => el && linkRefs.current.set(link.link_to, el)}
                  className={`whitespace-nowrap text-wrap balance text-sm md:text-lg lg:text-xl xl:text-2xl hover:text-slate-800 ${
                    location.pathname === link.link_to ? "text-rose-950" : ""
                  }`}
                >
                  {link.text}
                </Link>
              ) : (
                <div
                  className="whitespace-nowrap text-wrap balance text-sm md:text-lg lg:text-xl xl:text-2xl hover:text-slate-800 cursor-pointer relative"
                  onClick={(e) => e.preventDefault()}
                >
                  {link.text}
                  {/* Появление подменю только если текущий пункт меню наведен */}
                  {isHovered === link.id && renderSubmenu(link.submenu)}  
                </div>
              )}
            </div>
          ))}
        </nav>
      </div>

      <i className="fa-solid fa-user mr-5 text-4xl hover:text-slate-800 p-2"></i>
    </header>
  );
};

export default Header;
