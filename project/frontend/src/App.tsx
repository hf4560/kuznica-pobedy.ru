import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import News from "./pages/News";
import HelpUs from "./pages/HelpUs";
import ForDefenders from "./pages/ForDefenders";
import Contact from "./pages/Contact";
import './index.css';


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="novosti" element={<News />} />
        <Route path="svyazatsya" element={<Contact />} />
        <Route path="zashitnikam" element={<ForDefenders />} />
        <Route path="podderzhat" element={<HelpUs />} />
      </Route>
    </Routes>
  );
};

export default App;
