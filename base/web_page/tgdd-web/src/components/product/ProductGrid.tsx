import type { Product } from "../../types/ProductTypes";
import { ProductCard } from "./ProductCard";

export const ProductGrid = ({
  products,
}: {
  products: Record<string, Product>;
}) => {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
      {Object.values(products).map((product, index) => (
        <ProductCard key={index} product={product} />
      ))}
    </div>
  );
};
