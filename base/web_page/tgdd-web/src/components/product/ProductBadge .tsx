export const ProductBadge = ({
  type,
  text,
  urlImg
}: {
  type: "new" | "exclusive";
  text?: string;
  urlImg?: string;
}) => {
  return (
    <div
      className={`absolute ${
        type === "new" ? "top-2 left-2 bg-red-500" : "top-0 right-0"
      } z-10`}
    >
      {type === "new" ? (
        <span className="text-xs font-medium text-white px-2 py-1 rounded-md">
          {text || "Mẫu mới"}
        </span>
      ) : (
        <img
          src={urlImg}
          alt="Exclusive"
          className="w-10 h-10"
        />
      )}
    </div>
  );
};
