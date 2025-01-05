"use client";
import { useState, useEffect } from "react";
import { sendRequest } from "../../../services/api";
import { useRouter } from "next/navigation";

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

  // useEffect(() => {
  //   const token = localStorage.getItem("token");
  //   if (token) router.push("/");
  // }, [router]);

  const handleChange = (e: any) => {
    const { name, value } = e.target;
    setUser((pre) => ({ ...pre, [name]: value }));
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();

    if (user.password !== user.repassword && !user.email) {
      setMessage("Нууц үг таарахгүй байна");
      return;
    }

    try {
      setLoad(true);
      const data = await sendRequest(
        "http://127.0.0.1:8000/api/auth/",
        "post",
        JSON.stringify(user)
      );
      console.log(data);
      setMessage(data.resultMessage);
    } catch (e) {
      console.log(e);
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
    <>
      <h3>Register</h3>
      <p>{message}</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="lastname"
          placeholder="Овог"
          value={user.lastname}
          // onChange={setLastname((e) => e.target.value)}
          onChange={(e) => handleChange(e)}
          required
        />
        <br />
        <br />
        <input
          type="text"
          name="firstname"
          placeholder="Нэр"
          value={user.firstname}
          onChange={(e) => handleChange(e)}
          required
        />
        <br />
        <br />
        <input
          type="email"
          value={user.email}
          onChange={(e) => handleChange(e)}
          name="email"
          placeholder="email"
          required
        />
        <br />
        <br />
        <input
          type="password"
          name="password"
          onChange={(e) => handleChange(e)}
          placeholder="********"
          value={user.password}
          required
        />
        <br />
        <br />
        <input
          type="password"
          name="repassword"
          onChange={(e) => handleChange(e)}
          value={user.repassword}
          placeholder="********"
          required
        />
        <br />
        <br />
        <button type="submit" disabled={load}>
          {load ? "registering" : "register"}
        </button>
      </form>
    </>
  );
}
