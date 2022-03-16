import { Container, Box, Grid, Typography } from "@mui/material";

function Copyright() {
  return (
    <Typography variant="body1" color="common.white" align="center">
      {"Copyright © "}
      Recedivies Blogs {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const Footer = () => {
  return (
    <footer id="footer">
      <Box
        px={{ xs: 3, sm: 10 }}
        py={{ xs: 5, sm: 10 }}
        bgcolor="text.secondary"
        color="white"
      >
        <Container maxWidth="lg">
          <Grid container spacing={5}>
            <Copyright />
          </Grid>
        </Container>
      </Box>
    </footer>
  );
};

export default Footer;
