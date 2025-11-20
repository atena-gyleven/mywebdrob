import { NavLink } from "react-router-dom";

function Sidebar() {
  const links = [
    { to: "/", label: "Resumen" },
    { to: "/prendas", label: "Mi armario" },
    { to: "/looks", label: "Looks" },
    { to: "/calendario", label: "Calendario" },
    { to: "/comunidad", label: "Comunidad" },
  ];

  return (
    <aside className="sidebar">
      <nav>
        <ul>
          {links.map((link) => (
            <li key={link.to}>
              <NavLink
                to={link.to}
                end
                className={({ isActive }) =>
                  isActive ? "sidebar-link active" : "sidebar-link"
                }
              >
                {link.label}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </aside>
  );
}

export default Sidebar;