import WheelPagination from "@/components/ui/wheel-pagination";

export default function DemoPagination() {
  const handlePageChange = (page: number) => {
    console.log("Active Page:", page + 1);
  };

  return (
      <WheelPagination
        totalPages={50}        // Total number of pages
        visibleCount={7}       // Number of pages visible at once
        className="bg-white dark:bg-gray-800"
        onChange={handlePageChange} // Callback when page changes
      />
  );
}
