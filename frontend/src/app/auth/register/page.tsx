"use client";
import { useState, useEffect } from "react";
import { sendRequest } from "../../../services/api";
import { useRouter } from "next/navigation";

// router eer message damjuulah
export default function Register() {
  const router = useRouter();
  const [message, setMessage] = useState<string>("");
  const [user, setUser] = useState({
    action: "register",
    firstname: "",
    lastname: "",
    email: "",
    password: "",
    repassword: "",
  });
  const [load, setLoad] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) router.push("/");
  }, [router]);

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setUser((pre) => ({ ...pre, [name]: value }));
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      setLoad(true);

      if (user.password !== user.repassword || !user.email) {
        setMessage("Нууц үг таарахгүй байна");
        return;
      }

      const data = await sendRequest(
        "http://127.0.0.1:8000/api/auth/",
        "post",
        JSON.stringify(user)
      );
      setMessage(data.resultMessage);
    } catch (e) {
      setMessage("Сервер дотоод алдаа гарлаа");
    } finally {
      setTimeout(() => setMessage(""), 5000);
      setUser((pre) => ({
        ...pre,
        firstname: "",
        lastname: "",
        password: "",
        repassword: "",
        email: "",
      }));
      setLoad(false);
    }
  };

  return (
    <div style={{ width: "300px", margin: "0 auto" }}>
      <p>{message}</p>
      <form onSubmit={handleSubmit} className="form-control">
        <h1>Register</h1>
        <br />
        <input
          type="text"
          className="form-control"
          name="lastname"
          placeholder="Овог"
          value={user.lastname}
          onChange={(e) => handleChange(e)}
          required
        />
        <br />
        <input
          type="text"
          className="form-control"
          name="firstname"
          placeholder="Нэр"
          value={user.firstname}
          onChange={(e) => handleChange(e)}
          required
        />
        <br />
        <input
          type="email"
          value={user.email}
          onChange={(e) => handleChange(e)}
          name="email"
          className="form-control"
          placeholder="email"
          required
        />
        <br />
        <input
          type="password"
          name="password"
          onChange={(e) => handleChange(e)}
          placeholder="********"
          value={user.password}
          className="form-control"
          required
        />
        <br />
        <input
          type="password"
          name="repassword"
          onChange={(e) => handleChange(e)}
          value={user.repassword}
          placeholder="********"
          className="form-control"
          required
        />
        <br />
        <button
          type="submit"
          disabled={load}
          className="form-control btn btn-success"
        >
          {load ? "registering" : "register"}
        </button>
        <br />
        <br />
        <button
          type="button"
          onClick={() => router.push("/auth/login")}
          className="form-control btn btn-secondary"
        >
          to login
        </button>
      </form>
    </div>
  );
}
