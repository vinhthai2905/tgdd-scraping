export const Price = ({ current, old }: { current: string; old: string | null }) => {
  return (
    <div className="mt-2">
      <span className="text-red-600 font-bold">{current}</span>
      {old && (
        <span className="text-gray-400 text-xs line-through ml-2">{old}</span>
      )}
    </div>
  );
};
