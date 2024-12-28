export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <header>My Website Header</header>
        {children}
        <footer>My Website Footer</footer>
      </body>
    </html>
  );
}