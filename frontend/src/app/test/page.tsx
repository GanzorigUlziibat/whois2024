"use client";
import { useEffect, useState } from "react";

const MyComponent = () => {
  const [data, setData] = useState<null | string>(null);

  console.log(`tes###########${data}`)
  useEffect(() => {
    if (typeof window !== "undefined") {
      const storedData = localStorage.getItem("firstname");
      if (storedData) {
        setData(storedData);
      }
    }
  }, []); // Empty dependency array to run only once after the component mounts

  return (
    <div>
      {data ? (
        <p>Stored data: {data}</p>
      ) : (
        <p>No data stored in localStorage.</p>
      )}
    </div>
  );
};

export default MyComponent;
