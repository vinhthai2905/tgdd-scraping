import { useState } from "react";
import type { ProductChoice } from "../../types/ProductTypes";

export const ProductChoices = ({ choices }: { choices: ProductChoice[] }) => {
  const getMergedChoices = () => {
    const mergedChoices: string[] = [];
    for (let i = 0; i < choices.length; i++) {
      if (choices[i] === "-") {
        continue;
      }
      if (i > 0 && choices[i - 1] === "-") {
        mergedChoices[mergedChoices.length - 1] += ` - ${choices[i]}`;
      } else {
        mergedChoices.push(choices[i]);
      }
    }
    return mergedChoices;
  };

  const mergedChoices = getMergedChoices();
  const [selectedChoice, setSelectedChoice] = useState<string>(mergedChoices[0]); // Set default to the first merged choice

  return (
    <div className="flex flex-wrap gap-2 my-4">
      {mergedChoices.map((choice, index) => (
        <button
          key={index}
          onClick={() => setSelectedChoice(choice)}
          className={`text-xs px-2 py-1 border rounded-md transition-colors ${
            selectedChoice === choice
              ? "bg-yellow-500 text-white border-blue-500"
              : "border-gray-300 text-gray-700"
          }`}
        >
          {choice}
        </button>
      ))}
    </div>
  );
};
