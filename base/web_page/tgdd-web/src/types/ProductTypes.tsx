export type ProductChoice = string;

export type Product = {
  product_image: string;
  exclusive_tag: string | null;
  product_new: string | null;
  product_installment: string | null;
  product_name: string;
  product_tech: string;
  productChoices: ProductChoice[];
  product_price: string;
  old_price: string | null;
  gift: string | null;
  sold_quantity: string | null;
  star: string | null;
};