"use client";

import { sendRequest } from "@/services/api";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Login() {
  const router = useRouter();
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [user, setUser] = useState({
    action: "login",
    email: "",
    password: "",
  });

  const handSubmit = async (e: any) => {
    e.preventDefault();
    try {
      setLoading(true);
      const data = await sendRequest(
        "http://127.0.0.1:8000/api/auth/",
        "post",
        JSON.stringify(user)
      );
      if (data.resultCode === 200) {
        router.push("/");
        return;
      }
      setMessage(`${data.resultMessage}`);
    } catch (e) {
      setMessage(`Service алдаа: ${e}`);
    } finally {
      setTimeout(() => {
        setMessage("");
      }, 4000);
      setUser((pre) => ({ ...pre, action: "login", email: "", password: "" }));
      setLoading(false);
    }
  };

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setUser((pre) => ({ ...pre, [name]: value }));
  };

  return (
    <>
      <h1>Login</h1>
      <p>{message}</p>
      <form onSubmit={handSubmit}>
        <input
          type="email"
          value={user.email}
          name="email"
          onChange={handleChange}
          placeholder="email"
        />
        <br />
        <br />
        <input
          type="password"
          value={user.password}
          onChange={handleChange}
          name="password"
          placeholder="************"
        />
        <br />
        <br />
        <button type="submit" style={{ marginRight: "20px" }}>
          {loading ? "logining..." : "login"}
        </button>
      </form>
      <br />
      <button onClick={() => router.push("/auth/register")}>register</button>
    </>
  );
}
