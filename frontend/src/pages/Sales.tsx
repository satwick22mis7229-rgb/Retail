import { useEffect, useState } from "react";
import api from "../services/api";

interface Sale {
  id: number;
  customer_id: number;
  product_id: number;
  quantity: number;
  total_amount: number;
}

function Sales() {
  const [sales, setSales] = useState<Sale[]>([]);
  const [customers, setCustomers] = useState([]);
  const [products, setProducts] = useState([]);
  const [form, setForm] = useState({
    customer_id: "",
    product_id: "",
    quantity: "",
  });

  const getCustomerName = (id: number) => {
  const customer = customers.find(
    (c: any) => c.id === id
  );

  return customer ? customer.name : id;
};

const getProductName = (id: number) => {
  const product = products.find(
    (p: any) => p.id === id
  );

  return product ? product.name : id;
};

  const loadSales = () => {
    api.get("/customers/")
  .then((res) => setCustomers(res.data));

api.get("/products/")
  .then((res) => setProducts(res.data));
    api.get("/sales/")
      .then((res) => setSales(res.data))
      .catch(console.error);
  };

  useEffect(() => {
    loadSales();
  }, []);


  const addSale = () => {
    api.post("/sales/", null, {
      params: {
        customer_id: Number(form.customer_id),
        product_id: Number(form.product_id),
        quantity: Number(form.quantity),
      },
    })
    .then(() => {
      loadSales();

      setForm({
        customer_id: "",
        product_id: "",
        quantity: "",
      });
    })
    .catch(console.error);
  };

  const exportCSV = () => {
  let csv =
    "ID,Customer,Product,Quantity,Amount\n";

  sales.forEach((sale) => {
    csv += `${sale.id},${getCustomerName(
      sale.customer_id
    )},${getProductName(
      sale.product_id
    )},${sale.quantity},${sale.total_amount}\n`;
  });

  const blob = new Blob(
    [csv],
    { type: "text/csv;charset=utf-8;" }
  );

  const url = URL.createObjectURL(blob);

  const link = document.createElement("a");

  link.href = url;
  link.download = "sales_report.csv";

  document.body.appendChild(link);

  link.click();

  document.body.removeChild(link);
};

  return (
    <div className="p-6">

      <h1 className="text-4xl font-bold mb-6">
        Sales
      </h1>

      <div className="bg-white p-6 rounded-xl shadow">

        <select
  value={form.customer_id}
  onChange={(e) =>
    setForm({
      ...form,
      customer_id: e.target.value,
    })
  }
>
  <option value="">
    Select Customer
  </option>

  {customers.map((customer: any) => (
    <option
      key={customer.id}
      value={customer.id}
    >
      {customer.name}
    </option>
  ))}
</select>

        <select
  value={form.product_id}
  onChange={(e) =>
    setForm({
      ...form,
      product_id: e.target.value,
    })
  }
>
  <option value="">
    Select Product
  </option>

  {products.map((product: any) => (
    <option
      key={product.id}
      value={product.id}
    >
      {product.name}
    </option>
  ))}
</select>

        <input
          placeholder="Quantity"
          value={form.quantity}
          onChange={(e) =>
            setForm({
              ...form,
              quantity: e.target.value,
            })
          }
        />

        <button onClick={addSale}>
          Create Sale
        </button>
        <button
  onClick={exportCSV}
  className="bg-green-600 text-white px-4 py-2 rounded mb-4"
>
  Export Sales CSV
</button>

      </div>

      <table
        border={1}
        cellPadding={10}
        style={{
          width: "100%",
          marginTop: "20px",
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Customer</th>
            <th>Product</th>
            <th>Quantity</th>
            <th>Total Amount</th>
          </tr>
        </thead>

        <tbody>
          {sales.map((sale) => (
            <tr key={sale.id}>
              <td>{sale.id}</td>
              <td>{getCustomerName(sale.customer_id)}</td>
              <td>{getProductName(sale.product_id)}</td>
              <td>{sale.quantity}</td>
              <td>₹{sale.total_amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <button
  onClick={exportCSV}
  style={{
    marginBottom: "20px",
    padding: "10px",
  }}
>
  Export Sales CSV
</button>

    </div>
  );
}

export default Sales;