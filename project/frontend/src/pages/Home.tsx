import { useEffect } from 'react';

export default function Home() {
  useEffect(() => {
    // Динамически изменяем заголовок страницы
    document.title = 'Кузница Победы – Главная';
  }, []);
  return (
    <div className="h-screen flex items-center justify-center bg-gray-900 text-white">
      <h1 className="text-4xl font-bold">Home Page</h1>
    </div>
  );
}