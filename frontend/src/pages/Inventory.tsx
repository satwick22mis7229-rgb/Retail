import { useEffect, useState } from "react";
import api from "../services/api";

interface Inventory {
  id: number;
  product_id: number;
  quantity: number;
}

function Inventory() {
  const [form, setForm] = useState({
  product_id: "",
  quantity: "",
});
  const [inventory, setInventory] = useState<Inventory[]>([]);
  const [products, setProducts] = useState<any[]>([]);

  useEffect(() => {
  loadInventory();

  api.get("/products/")
    .then((res) => setProducts(res.data))
    .catch(console.error);

}, []);

  const loadInventory = () => {
    api.get("/inventory/")
      .then((res) => setInventory(res.data))
      .catch(console.error);
  };
  const addInventory = () => {
  api.post(
    `/inventory/?product_id=${form.product_id}&quantity=${form.quantity}`
  )
  .then(() => {
    loadInventory();

    setForm({
      product_id: "",
      quantity: "",
    });
  })
  .catch(console.error);
};
const getProductName = (productId: number) => {
  const product = products.find(
    (p: any) => p.id === productId
  );

  return product ? product.name : productId;
};

  return (
    <div style={{ padding: "20px" }}>
      <h1>Inventory</h1>
      <div style={{ marginBottom: "20px" }}>
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

  <button onClick={addInventory}>
    Add Inventory
  </button>
</div>

      <table
        border={1}
        cellPadding={10}
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "20px",
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
           <th>Product Name</th>
            <th>Quantity</th>
          </tr>
        </thead>

        <tbody>
          {inventory.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
             <td>{getProductName(item.product_id)}</td>
              <td>{item.quantity}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Inventory;