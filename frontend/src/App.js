import * as React from "react";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import Crawl from "./Crawl";

export default function BasicModal() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <div>
      <Button
        sx={{
          width: "40%",
          bgcolor: "#262525",
          border: "2px solid #262525",
          p: 4,
        }}
        onClick={handleOpen}
      >
        Open modal
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box
          sx={{
            position: "absolute",
            top: "50%",
            left: "50%",
            transform: "translate(-50%, -50%)",
            width: "90%",
            height: "100%",
            bgcolor: "black",
            border: "2px solid #262525",
            boxShadow: 24,
            p: 4,
          }}
        >
          <Crawl
            _intro="Not so long ago, in an office not so far,\n far away...."
            episodeNumber="Episode 0"
            episodeTitle="SNOWFLAKE AND ML: A LOVE STORY"
            _content='[""]'
          />
        </Box>
      </Modal>
    </div>
  );
}
