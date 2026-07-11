import { useEffect, useState } from "react";
import api from "../services/api";
import RevenueChart from "../components/RevenueChart";

interface DashboardData {
  total_products: number;
  total_customers: number;
  total_sales: number;
  total_revenue: number;
}

function Dashboard() {
  
  const [profit, setProfit] = useState(0);
  const [lowStock, setLowStock] = useState<any[]>([]);
  const [stats, setStats] = useState<DashboardData>({
    total_products: 0,
    total_customers: 0,
    total_sales: 0,
    total_revenue: 0,
  });
  const downloadReport = () => {
  window.open(
    "http://127.0.0.1:8000/sales/report",
    "_blank"
  );
};
  const [topProducts, setTopProducts] =
  useState<any[]>([]);

  useEffect(() => {
    api.get("/dashboard/top-products")
  .then((res) => setTopProducts(res.data))
  .catch(console.error);
    api.get("/dashboard/profit")
      .then((res) => setProfit(res.data.profit))
      .catch(console.error);

    api.get("/inventory/low-stock")
      .then((res) => setLowStock(res.data))
      .catch(console.error);

    api.get("/dashboard/")
      .then((res) => setStats(res.data))
      .catch(console.error);
  }, []);

  return (
   <div className="p-8 bg-slate-100 min-h-screen">
      <div className="mb-8">
  <h1 className="text-5xl font-bold text-slate-800">
    Smart Retail Intelligence Platform
  </h1>

  <p className="text-gray-500 mt-2">
    Inventory, Sales and Revenue Analytics Dashboard
  </p>
</div>
<div
  style={{
    background: "white",
    padding: "20px",
    borderRadius: "12px",
    marginBottom: "20px",
    boxShadow: "0px 2px 8px rgba(0,0,0,0.1)",
  }}
>
  <h2>Business Overview</h2>

  <p>
    Revenue: ₹{stats.total_revenue}
  </p>

  <p>
    Profit: ₹{profit}
  </p>

  <p>
    Products: {stats.total_products}
  </p>

  <p>
    Customers: {stats.total_customers}
  </p>
</div>

      <h2 style={{ marginTop: "30px" }}>
        Low Stock Alerts
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6 mt-5">

        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-gray-500 text-lg">Products</h3>
          <h1 className="text-4xl font-bold mt-2">
            {stats.total_products}
          </h1>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-gray-500 text-lg">Customers</h3>
          <h1 className="text-4xl font-bold mt-2">
            {stats.total_customers}
          </h1>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-gray-500 text-lg">Sales</h3>
          <h1 className="text-4xl font-bold mt-2">
            {stats.total_sales}
          </h1>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-gray-500 text-lg">Revenue</h3>
          <h1 className="text-4xl font-bold mt-2">
            ₹{stats.total_revenue}
          </h1>
        </div>
        

        <div className="bg-white rounded-xl shadow-lg p-6">
          <h3 className="text-gray-500 text-lg">Profit</h3>
          <h1 className="text-4xl font-bold mt-2">
            ₹{profit}
          </h1>
        </div>

      </div>

      <div style={{ marginTop: "40px" }}>
        <RevenueChart />
      </div>
      <div
  className="bg-white rounded-xl shadow-lg p-6 mt-6"
>
  <h2 className="text-2xl font-bold mb-4">
    Top Selling Products
  </h2>

  {topProducts.map((item) => (
    <div key={item.product_id}>
      Product {item.product_id}
      — Sold {item.total}
    </div>
  ))}
</div>
<button
  onClick={downloadReport}
  className="bg-green-600 text-white px-4 py-2 rounded mt-4"
>
  Download Sales Report
</button>

      {lowStock.length === 0 ? (
        <p>No low stock products</p>
      ) : (
        lowStock.map((item: any) => (
          <div
            key={item.id}
            style={{
              background: "#ffe5e5",
              padding: "10px",
              marginTop: "10px",
              borderRadius: "8px",
            }}
          >
           <div
  className="
  bg-red-100
  border-l-4
  border-red-500
  text-red-700
  p-4
  rounded
  mt-2
  "
>
  ⚠ Product {item.product_id} has only
  {" "}
  {item.quantity}
  {" "}
  items left
</div>
          </div>
        ))
      )}
    </div>
  );
}

export default Dashboard;