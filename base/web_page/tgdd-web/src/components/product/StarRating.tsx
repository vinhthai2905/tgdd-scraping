export const StarRating = ({ rating }: { rating: string | null }) => {
  let ratingNum = 0;
  if (!rating) {
    ratingNum = 0;
    rating = '0 đánh giá';
  } else ratingNum = parseFloat(rating);

  return (
    <div className="flex items-center gap-1">
      {[1, 2, 3, 4, 5].map((star) => (
        <div key={star} className="text-yellow-400">
          {ratingNum >= star ? "★" : "☆"}
        </div>
      ))}
      <span className="text-xs text-gray-600 ml-1">{rating}</span>
    </div>
  );
};
