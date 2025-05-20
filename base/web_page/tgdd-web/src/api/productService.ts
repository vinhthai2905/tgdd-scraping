import type { Product } from '../types/ProductTypes';
import axiosInstance from './axios';

export const getAllProducts = async (): Promise<Product[]> => {
  const response = await axiosInstance.get('/products');
  return response.data;
};

export const searchProducts = async (query: string): Promise<Product[]> => {
  const response = await axiosInstance.get(`/search?q=${encodeURIComponent(query)}`);
  return response.data;
};

export const getProductsByCategory = async (category: string): Promise<Product[]> => {
  const response = await axiosInstance.get(`/site/${encodeURIComponent(category)}/products`);
  return response.data;
};
  