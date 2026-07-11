import { useState } from "react";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const login = () => {
    if (
      email === "admin@gmail.com" &&
      password === "admin123"
    ) {
      localStorage.setItem("loggedIn", "true");

      window.location.href = "/";
    } else {
      alert("Invalid Credentials");
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-100">

      <div className="bg-white p-8 rounded-xl shadow-lg w-96">

        <h1 className="text-3xl font-bold mb-6">
          Login
        </h1>

        <input
          className="border p-2 w-full mb-3"
          placeholder="Email"
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
        />

        <input
          type="password"
          className="border p-2 w-full mb-3"
          placeholder="Password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
        />

        <button
          onClick={login}
          className="bg-blue-600 text-white w-full p-2 rounded"
        >
          Login
        </button>

      </div>

    </div>
  );
}

export default Login;