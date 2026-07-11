import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div
      className="bg-slate-800 text-white p-5"
      style={{
        width: "250px",
        minHeight: "100vh",
      }}
    >
      <h2 className="text-2xl font-bold mb-6">
        Retail AI
      </h2>

      <div className="space-y-4">

        <Link to="/">Dashboard</Link>
        <br />

        <Link to="/products">Products</Link>
        <br />

        <Link to="/customers">Customers</Link>
        <br />

        <Link to="/inventory">Inventory</Link>
        <br />

        <Link to="/sales">Sales</Link>

      </div>
    </div>
  );
}

export default Sidebar;