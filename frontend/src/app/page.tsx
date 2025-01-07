
export default function HomePage() {
  return (
    <div>
      <div
        id="carouselExample"
        className="carousel slide pointer-event"
        data-bs-ride="carousel"
      >
        <div className="carousel-inner">
          <div className="carousel-item active">
            <img
              src="/lion.png"
              style={{ height: "300px", objectFit: "contain" }}
              className="d-block w-100"
              alt="First Slide"
            />
          </div>
          <div className="carousel-item">
            <img
              style={{ height: "300px", objectFit: "contain" }}
              src="/zebra.png"
              className="d-block w-100"
              alt="Second Slide"
            />
          </div>
          <div className="carousel-item">
            <img
              src="/cheetah.png"
              style={{ height: "300px", objectFit: "contain" }}
              className="d-block w-100"
              alt="Third Slide"
            />
          </div>
        </div>

        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExample"
          data-bs-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselExample"
          data-bs-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  );
}
