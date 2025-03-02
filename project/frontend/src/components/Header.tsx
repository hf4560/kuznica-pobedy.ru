import { Link, useLocation } from "react-router-dom";
import logo from "../assets/logo.png";

const Header = () => {
  const location = useLocation();

  return (
    <header className="w-full bg-stone-200 text-white border-b border-stone-300">
      <div className="p-4 flex justify-between items-center max-w-screen-xl mx-auto">
        <nav className="flex items-center space-x-6">
          <Link to="/" className="flex items-center">
            <img 
              src={logo} 
              alt="ЛОГО" 
              className="h-10 w-auto"
            />
          </Link>
          
          <Link 
            to="/novosti" 
            className={`text-lg hover:text-green-400 transition-colors ${
              location.pathname === '/novosti' ? 'text-green-400 font-medium' : ''
            }`}
          >
            НОВОСТИ
          </Link>
          <Link 
            to="/zashitnikam" 
            className={`text-lg hover:text-green-400 transition-colors ${
              location.pathname === '/zashitnikam' ? 'text-green-400 font-medium' : ''
            }`}
          >
            ЗАЩИТНИКАМ
          </Link>
          <Link 
            to="/svyazatsya" 
            className={`text-lg hover:text-green-400 transition-colors ${
              location.pathname === '/svyazatsya' ? 'text-green-400 font-medium' : ''
            }`}
          >
            СВЯЗЯТЬСЯ
          </Link>
          <Link 
            to="/podderzhat" 
            className={`text-lg hover:text-green-400 transition-colors ${
              location.pathname === '/podderzhat' ? 'text-green-400 font-medium' : ''
            }`}
          >
            ПОДДЕРЖАТЬ НАС
          </Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;