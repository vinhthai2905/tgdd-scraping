import { useEffect, useState } from "react";
import "./App.css";
import type { Product } from "./types/ProductTypes";
import { ProductGrid } from "./components/product/ProductGrid";
import phonesData from "./assets/data/phones.json";

function App() {
  const [phones, setPhones] = useState<Record<string, Product>>(phonesData);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);

    const timer = setTimeout(() => {
      setPhones(phonesData);
      setLoading(false);
    }, 500);

    return () => clearTimeout(timer);
  }, []);
  return (
    <>
      <header className="bg-white shadow-md py-6 mb-6">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-3xl font-extrabold text-gray-800">
            Thái Bảo Tráng Dương
          </h1>
          <p className="text-lg text-gray-600 mt-2">
            Diệt trừ cái ác, bảo vệ thế giới
          </p>
        </div>
      </header>

      <main className=" mx-auto px-4 pb-8">
        <div className="bg-white p-4 rounded-lg mb-6">
          <div className="flex justify-between items-center">
            <h2 className="text-lg font-semibold">Danh sách sản phẩm</h2>
            <div className="flex gap-4">
              <select className="border rounded px-2 py-1 text-sm">
                <option>Giá thấp đến cao</option>
                <option>Giá cao đến thấp</option>
              </select>
              <select className="border rounded px-2 py-1 text-sm">
                <option>Tất cả mục</option>
                <option>Điện thoại</option>
                <option>Tablet</option>
                <option>Laptop</option>
              </select>
            </div>
          </div>
        </div>

        {loading ? (
          <div className="text-center py-12">
            <div className="inline-block animate-spin h-8 w-8 border-4 border-gray-300 border-t-blue-500 rounded-full"></div>
            <p className="mt-4 text-gray-600">Loading products...</p>
          </div>
        ) : (
          <div className="slideUp">
            <ProductGrid products={phones} />
          </div>
        )}
      </main>

      <footer className="bg-white border-t border-gray-200 py-6 mt-12">
        <div className="container mx-auto px-4 text-center text-gray-500 text-sm">
          <p>© 2025 Thái Bảo Tráng Dương. All rights reserved.</p>
        </div>
      </footer>
    </>
  );
}

export default App;
