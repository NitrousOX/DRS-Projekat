import { Link, NavLink } from "react-router-dom";
import "./Navbar.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo or brand name */}
        <Link to="/" className="navbar-logo">
          MyApp
        </Link>

        {/* Navigation links */}
        <div className="navbar-links">
          <NavLink 
            to="/" 
            className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}
          >
            Home
          </NavLink>

          <NavLink 
            to="/registration-list" 
            className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}
          >
            List
          </NavLink>

          
          <NavLink 
            to="/login" 
            className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}
          >
            Login
          </NavLink>
        </div>
      </div>
    </nav>
  );
}