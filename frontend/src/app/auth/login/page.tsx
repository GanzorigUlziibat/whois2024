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
        // "http://127.0.0.1:8000/api/auth/",
        "http://whoism.mandakh.org/api/auth/",
        "post",
        JSON.stringify(user)
      );
      if (data.resultCode === 200) {
        console.log(JSON.stringify(data));
        localStorage.setItem("firstname", data.data[0].firstname);
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
    <div style={{ width: "300px", margin: "0 auto" }}>
      <p>{message}</p>
      <form onSubmit={handSubmit} className="form-control">
        <h1>Login</h1>
        <br />
        <input
          type="email"
          value={user.email}
          name="email"
          onChange={handleChange}
          placeholder="Email"
          className="form-control"
          required
        />

        <br />
        <input
          type="password"
          value={user.password}
          onChange={handleChange}
          name="password"
          placeholder="************"
          className="form-control"
          required
        />
        <br />
        <button type="submit" className="form-control btn btn-success">
          {loading ? "logining..." : "login"}
        </button>
        <br />
        <br />
        <button
          type="button"
          onClick={() => router.push("/auth/register")}
          className="form-control btn btn-primary"
        >
          register
        </button>
      </form>
    </div>
  );
}
