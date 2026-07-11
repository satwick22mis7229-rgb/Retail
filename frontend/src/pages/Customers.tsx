import { useEffect, useState } from "react";
import api from "../services/api";

interface Customer {
  id: number;
  name: string;
  email: string;
  phone: string;
  address: string;
}

function Customers() {
  const [customers, setCustomers] = useState<Customer[]>([]);

  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    address: "",
  });

  const loadCustomers = () => {
    api.get("/customers/")
      .then((res) => setCustomers(res.data))
      .catch(console.error);
  };
  

  useEffect(() => {
    loadCustomers();
  }, []);

  const addCustomer = () => {
    api.post("/customers/", form)
      .then(() => {
        loadCustomers();

        setForm({
          name: "",
          email: "",
          phone: "",
          address: "",
        });
      })
      .catch(console.error);
  };

  return (
    <div className="p-6">

      <h1 className="text-4xl font-bold mb-6">
        Customers
      </h1>

      <div className="bg-white p-6 rounded-xl shadow">

        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />

        <input
          placeholder="Email"
          value={form.email}
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
        />

        <input
          placeholder="Phone"
          value={form.phone}
          onChange={(e) =>
            setForm({ ...form, phone: e.target.value })
          }
        />

        <input
          placeholder="Address"
          value={form.address}
          onChange={(e) =>
            setForm({ ...form, address: e.target.value })
          }
        />

        <button onClick={addCustomer}>
          Add Customer
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
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
          </tr>
        </thead>

        <tbody>
          {customers.map((customer) => (
            <tr key={customer.id}>
              <td>{customer.id}</td>
              <td>{customer.name}</td>
              <td>{customer.email}</td>
              <td>{customer.phone}</td>
              <td>{customer.address}</td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
}

export default Customers;