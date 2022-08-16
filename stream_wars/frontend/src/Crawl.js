import gsap from "gsap";
import React, { useEffect, useRef, useState } from "react";

import "./Crawl.css";
import volumeOff from "../public/volume_off.svg";
import volumeOn from "../public/volume_on.svg";

function Crawl({ intro, title, episodeNumber, episodeTitle, content }) {
  const introAnimation = useRef();
  const titleAnimation = useRef();
  const contentAnimation = useRef();
  const audioAnimation = useRef();

  const [muted, setMuted] = useState(true);

  useEffect(() => {
    let tl = new gsap.timeline();

    tl.to(introAnimation.current, {
      opacity: 1,
      delay: 1,
      duration: 4.5,
    })
      .to(introAnimation.current, {
        opacity: 0,
        duration: 1.5,
        onComplete: () => {
          if (audioAnimation.current !== null) {
            audioAnimation.current.play();
          }
        },
      })
      .set(titleAnimation.current, { opacity: 1, scale: 2.75, delay: 0.5 })
      .to(titleAnimation.current, { scale: 0.05, ease: "power2", duration: 8 })
      .to(titleAnimation.current, { opacity: 0, duration: 1.5 }, "-=1.5")
      .to(contentAnimation.current, { top: "-170%", duration: 200 });
  }, []);

  return (
    <div className="container">
      <section className="intro" ref={introAnimation}>
        <p>{intro}</p>
      </section>
      <section className="title" ref={titleAnimation}>
        <p>{title.toLowerCase()}</p>
      </section>
      <section className="crawl">
        <div className="content" ref={contentAnimation}>
          <h1 className="episode-number">{episodeNumber}</h1>
          <h2 className="episode-title">{episodeTitle}</h2>
          <p>{content}</p>
        </div>
      </section>
      <audio ref={audioAnimation} muted>
        <source
          type="audio/mpeg"
          src="https://ia801501.us.archive.org/23/items/StarWars_20180709/Star%20Wars.mp3"
        />
      </audio>
      <button
        className="volume"
        type="button"
        onClick={() => {
          audioAnimation.current.muted = !muted;
          setMuted(!muted);
        }}
      >
        {muted ? (
          <img src={volumeOff} alt="Volume is off" />
        ) : (
          <img src={volumeOn} alt="Volume is on" />
        )}
      </button>
    </div>
  );
}

export default Crawl;
