import { Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import Home from "./pages/Home";
import News from "./pages/News";
import HelpUs from "./pages/HelpUs";
import ForDefenders from "./pages/ForDefenders";
import Contact from "./pages/Contact";
import Structure from "./pages/Structure";
import Contacts from "./pages/Contacts";
import Reviews from "./pages/Reviews";
import ForNewVolunteers from "./pages/ForNewVolunteers";
import Instructions from "./pages/Instructions";
import './index.css';


const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="news" element={<News />} />
        <Route path="contact" element={<Contact />} />
        <Route path="defenders" element={<ForDefenders />} />
        <Route path="support" element={<HelpUs />} />
        <Route path="about/structure" element={<Structure />} />
        <Route path="about/contacts" element={<Contacts />} />
        <Route path="about/reviews" element={<Reviews />} />
        <Route path="volunteers/new" element={<ForNewVolunteers />} />
        <Route path="volunteers/instructions" element={<Instructions />} />
      </Route>
    </Routes>
  );
};

export default App;
