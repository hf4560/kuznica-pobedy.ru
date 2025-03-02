import { useEffect } from 'react';

export default function ForDefenders() {
  useEffect(() => {
    // Динамически изменяем заголовок страницы
    document.title = 'Кузница Победы – Защитникам';
  }, []);
  return (
    <div className="h-screen flex items-center justify-center bg-gray-900 text-white">
      <h1 className="text-4xl font-bold">For Defenders Page</h1>
    </div>
  );
}