import type { Product } from "../../types/ProductTypes";
import { Gift } from "./Gift";
import { Price } from "./Price";
import { ProductBadge } from "./ProductBadge ";
import { ProductChoices } from "./ProductChoice";
import { StarRating } from "./StarRating";

export const ProductCard = ({ product }: { product: Product }) => {
  return (
    <div className="group bg-white rounded-lg shadow-md overflow-hidden transition-all duration-300 hover:shadow-xl relative w-full hover:bg-gray-50 transform hover:-translate-y-1 border border-transparent hover:border-gray-200">
      <div className="relative pt-[100%] overflow-hidden">
        <img
          src={product.product_image}
          alt={product.product_name}
          className="absolute top-0 left-0 w-full h-full object-contain p-4 transition-all duration-500 group-hover:scale-105 group-hover:brightness-105"
        />

        <div className="absolute inset-0 bg-gradient-to-t from-transparent to-white/10 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

        {product.product_new && (
          <ProductBadge type="new" text={product.product_new} />
        )}
        {product.exclusive_tag && (
          <ProductBadge type="exclusive" urlImg={product.exclusive_tag} />
        )}
      </div>

      <div className="p-4 transition-all duration-300 group-hover:bg-gradient-to-b group-hover:from-gray-50 group-hover:to-white">
        <h3 className="font-semibold text-gray-800 line-clamp-2 group-hover:text-blue-600 transition-colors duration-300">
          {product.product_name}
        </h3>
        <p className="text-gray-500 text-sm mt-1 transition-colors duration-300 group-hover:text-gray-700">
          {product.product_tech}
        </p>

        <ProductChoices choices={product.productChoices} />

        <div className="transition-transform duration-300 group-hover:scale-105 transform origin-left">
          <Price current={product.product_price} old={product.old_price} />
        </div>

        <div className="transition-all duration-300 group-hover:translate-x-1">
          <Gift text={product.gift} />
        </div>

        <div className="mt-3 flex justify-between items-center">
          <StarRating rating={product.star} />
          <span className="text-xs text-gray-500 transition-all duration-300 group-hover:font-medium">
            {product.sold_quantity || "• Đã bán 0"}
          </span>
        </div>

        <div className="absolute bottom-4 left-0 right-0 flex justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-500 transform translate-y-4 group-hover:translate-y-0">
          <button className="bg-blue-500 hover:bg-blue-600 text-white text-xs font-medium py-1 px-3 rounded-full transition-colors duration-300 shadow-md">
            View details
          </button>
        </div>
      </div>
    </div>
  );
};
