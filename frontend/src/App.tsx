import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import UpcomingTrails from "./pages/UpcomingTrails";
import CompletedTrails from "./pages/CompletedTrails";
import Home from "./pages/Home";
import About from "./pages/about";


function App() {
  

      return(
      <div>
        <nav>
            <ul className="flex space-x-4 mt-4">
              <li>
                <Link to="/" className="text-stone-400 hover:text-stone-200 transition-colors">Home</Link>
              </li>
                <li>
                    <Link to="/about" className="text-stone-400 hover:text-stone-200 transition-colors">About</Link>
                </li>
                <li>
                    <Link to="/completed" className="text-stone-400 hover:text-stone-200 transition-colors">Completed Trails</Link>
                </li>
                <li>
                    <Link to="/upcoming" className="text-stone-400 hover:text-stone-200 transition-colors">Upcoming trails</Link>
                </li>
            </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/About" element={<About />} />
          <Route path="/completed" element={<CompletedTrails />} />
          <Route path="/upcoming" element={<UpcomingTrails />} />
        </Routes>
      </div>
      )
}

export default App;