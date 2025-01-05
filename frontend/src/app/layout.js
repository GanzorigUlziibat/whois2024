export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header>
          <ul>
            <li>
              <a href="/">Home</a>
            </li>
            <li>
              <a href="/auth/register">Register</a>
            </li>
          </ul>
        </header>
        <hr />

        {children}
        <hr />
        <footer>My Website Footer</footer>
      </body>
    </html>
  );
}
