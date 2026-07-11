import { useEffect, useState } from "react";
import api from "../services/api";

interface Product {
  id: number;
  name: string;
  sku: string;
  price: number;
  cost_price: number;
  description: string;
}

function Products() {
  const [editingId, setEditingId] = useState<number | null>(null);
  const [search, setSearch] = useState("");
 const deleteProduct = async (id: number) => {
  try {
    await api.delete(`/products/${id}`);

    const res = await api.get("/products/");
    setProducts(res.data);

    alert("Product Deleted");
  } catch (err) {
    console.error(err);
  }
};
  const [form, setForm] = useState({
    name: "",
    sku: "",
    price: "",
    cost_price: "",
    description: "",
  });
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    api.get("/products/")
      .then((res) => setProducts(res.data))
      .catch(console.error);
  }, []);

  const addProduct = async () => {
  try {
    await api.post("/products/", {
      name: form.name,
      sku: form.sku,
      price: Number(form.price),
      cost_price: Number(form.cost_price),
      description: form.description,
    });

    alert("Product Added Successfully");

    const res = await api.get("/products/");
    setProducts(res.data);

    setForm({
      name: "",
      sku: "",
      price: "",
      cost_price: "",
      description: "",
    });

  } catch (error) {
    console.error(error);
  }
};

  return (
    <div style={{ padding: "20px" }}>
      <h1>Products</h1>
      <input
  placeholder="Search Product"
  value={search}
  onChange={(e) => setSearch(e.target.value)}
/>

      <table
        border={1}
        cellPadding={10}
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "20px"
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>SKU</th>
            <th>Price</th>
            <th>Cost Price</th>
            <th>Description</th>
            <th>Actions</th>

          </tr>
        </thead>

        <tbody>
  {products
    .filter((p) =>
      p.name.toLowerCase().includes(
        search.toLowerCase()
      )
    )
    .map((product) => (
      <tr key={product.id}>
        <td>{product.id}</td>
        <td>{product.name}</td>
        <td>{product.sku}</td>
        <td>₹{product.price}</td>
        <td>₹{product.cost_price}</td>
        <td>{product.description}</td>
        <td>
  <button
    onClick={() => {
      setEditingId(product.id);

      setForm({
        name: product.name,
        sku: product.sku,
        price: String(product.price),
        cost_price: String(product.cost_price),
        description: product.description,
      });
    }}
  >
    Edit
  </button>

  <button
    onClick={() => deleteProduct(product.id)}
  >
    Delete
  </button>
</td>
      </tr>
    ))}
</tbody>
      </table>
      <div style={{ marginBottom: "20px" }}>
  <input
    placeholder="Name"
    value={form.name}
    onChange={(e) =>
      setForm({ ...form, name: e.target.value })
    }
  />

  <input
    placeholder="SKU"
    value={form.sku}
    onChange={(e) =>
      setForm({ ...form, sku: e.target.value })
    }
  />

  <input
    placeholder="Price"
    value={form.price}
    onChange={(e) =>
      setForm({ ...form, price: e.target.value })
    }
  />

  <input
    placeholder="Cost Price"
    value={form.cost_price}
    onChange={(e) =>
      setForm({ ...form, cost_price: e.target.value })
    }
  />

  <input
    placeholder="Description"
    value={form.description}
    onChange={(e) =>
      setForm({ ...form, description: e.target.value })
    }
  />

  <button onClick={addProduct}>
    Add Product
  </button>
</div>
    </div>
  );
}

export default Products;