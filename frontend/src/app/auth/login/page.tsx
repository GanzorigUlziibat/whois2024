"use client";
import React, { useState, useEffect } from "react";

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log("Interval is running...");

    return () => {
      console.log("Interval cleared");
    };
  }, []); // Зөвхөн анхны ачаалалд ажиллана.

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  );
}

export default App;
