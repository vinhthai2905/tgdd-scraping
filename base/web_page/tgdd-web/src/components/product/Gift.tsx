export const Gift = ({ text }: { text: string | null }) => {
  if (!text) return null;

  return (
    <div className="flex items-center gap-2 p-3 bg-gray-50 text-xs rounded-lg border border-gray-200 shadow-sm">
      <span className="inline-block bg-red-100 text-red-600 px-1 rounded mr-1">
        🎁
      </span>
      <span className="text-gray-700 truncate max-w-[100%]">
        {text}
      </span>
    </div>
  );
};
