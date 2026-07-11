import { Link } from "react-router-dom";

function Layout({ children }: any) {
  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>

      <div
  style={{
    width: "260px",
    background: "#0f172a",
    color: "white",
    padding: "25px",
    boxShadow: "2px 0px 10px rgba(0,0,0,0.2)",
  }}
>
      <h2
  style={{
    fontSize: "28px",
    fontWeight: "bold",
    marginBottom: "20px",
  }}
>
  🛒 Smart Retail 
</h2>

        <nav
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "15px",
            marginTop: "30px",
          }}
        >
          <Link to="/" style={link}>
            Dashboard
          </Link>

          <Link to="/products" style={link}>
            Products
          </Link>

          <Link to="/customers" style={link}>
            Customers
          </Link>

          <Link to="/inventory" style={link}>
            Inventory
          </Link>

          <Link to="/sales" style={link}>
            Sales
          </Link>
        </nav>
      </div>

      <div
        style={{
          flex: 1,
          background: "#f8fafc",
          padding: "20px",
        }}
      >
        {children}
      </div>

    </div>
  );
}

const link = {
  color: "white",
  textDecoration: "none",
  padding: "12px",
  borderRadius: "8px",
  background: "#1e293b",
};

export default Layout;