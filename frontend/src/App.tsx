import { Routes, Route } from "react-router-dom";

import Login from "./pages/Login";
import Signup from "./pages/Signup";

import Dashboard from "./pages/Dashboard";
import Products from "./pages/Products";
import Customers from "./pages/Customers";
import Inventory from "./pages/Inventory";
import Sales from "./pages/Sales";

import Layout from "./components/Layout";

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/" element={<Dashboard />} />
        <Route path="/products" element={<Products />} />
        <Route path="/customers" element={<Customers />} />
        <Route path="/inventory" element={<Inventory />} />
        <Route path="/sales" element={<Sales />} />
      </Routes>
    </Layout>
  );
}

export default App;