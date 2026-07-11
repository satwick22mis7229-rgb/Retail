import { useState } from "react";

function Signup() {
  const [name,setName] = useState("");
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");

  const signup = () => {
    alert("User Registered");
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-gray-100">

      <div className="bg-white p-8 rounded-xl shadow-lg w-96">

        <h1 className="text-3xl font-bold mb-6">
          Sign Up
        </h1>

        <input
          className="border p-2 w-full mb-3"
          placeholder="Name"
          value={name}
          onChange={(e)=>setName(e.target.value)}
        />

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
          onClick={signup}
          className="bg-green-600 text-white w-full p-2 rounded"
        >
          Sign Up
        </button>

      </div>

    </div>
  );
}

export default Signup;