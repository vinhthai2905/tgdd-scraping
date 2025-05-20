import type { Product } from '../types/ProductTypes'
import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: '', // use relative paths; NGINX handles routing
  headers: {
    'Content-Type': 'application/json',
  },
})

export const getAllProducts = async (): Promise<Product[]> => {
  const response = await axiosInstance.get('/database_api/products')
  return response.data
}

export const searchProducts = async (query: string): Promise<Product[]> => {
  const response = await axiosInstance.get(`/database_api/search?q=${encodeURIComponent(query)}`)
  return response.data
}

export const getProductsByCategory = async (category: string): Promise<Product[]> => {
  const response = await axiosInstance.get(`/database_api/site/${encodeURIComponent(category)}/products`)
  return response.data
}