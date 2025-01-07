"use client";
import { usePathname, useRouter } from "next/navigation";
import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

export default function RootLayout({ children }: any) {
  const pathName = usePathname();
  const router = useRouter();
  const [fname, setFname] = useState<string | null>(null); // `null` болгон өөрчиллөө

  const hideLayout =
    pathName === "/auth/login" || pathName === "/auth/register";

  useEffect(() => {
    const storedFname = localStorage.getItem("firstname");
    if (storedFname) {
      setFname(storedFname); // Хэрэв localStorage-д байна уу гэдгийг шалгах
    }
  }, [hideLayout]);

  return (
    <html lang="en">
      <body>
        {!hideLayout && (
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="/">
              WHOIS
            </a>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarSupportedContent"
              aria-controls="navbarSupportedContent"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>

            <div
              className="collapse navbar-collapse"
              id="navbarSupportedContent"
            >
              <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <a className="nav-link active" href="/">
                    Home <span className="visually-hidden">(current)</span>
                  </a>
                </li>

                {fname ? (
                  <li className="nav-item">
                    <a
                      className="nav-link"
                      href="/"
                      onClick={() => {
                        localStorage.removeItem("firstname");
                      }}
                    >
                      Logout ({fname})
                    </a>
                  </li>
                ) : (
                  <>
                    <li className="nav-item">
                      <a className="nav-link" href="/auth/login">
                        Login
                      </a>
                    </li>
                    <li className="nav-item">
                      <a className="nav-link" href="/auth/register">
                        Register
                      </a>
                    </li>
                  </>
                )}
              </ul>
              <form className="d-flex">
                <input
                  className="form-control me-2"
                  type="search"
                  placeholder="Search"
                  aria-label="Search"
                />
                <button className="btn btn-outline-success" type="submit">
                  Search
                </button>
              </form>
            </div>
          </nav>
        )}
        <div className="container">{children}</div>
      </body>
    </html>
  );
}
