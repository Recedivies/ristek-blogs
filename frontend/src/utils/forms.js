export const onSubmit = (e, submitCallback) => {
  e.preventDefault();
  submitCallback();
};

export const submitWithEnter = (e, submitCallback) => {
  if (e.key === "Enter") {
    e.preventDefault();
    submitCallback();
  }
};
