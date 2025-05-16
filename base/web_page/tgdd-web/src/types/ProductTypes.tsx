export type ProductChoice = string;

export type Product = {
  productImage: string;
  exclusiveTag: string | null;
  productNew: string | null;
  productInstallment: string | null;
  productName: string;
  productTech: string;
  productChoices: ProductChoice[];
  productPrice: string;
  oldPrice: string | null;
  gift: string | null;
  soldQuantity: string | null;
  star: string | null;
};