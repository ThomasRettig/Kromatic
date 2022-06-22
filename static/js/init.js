function readURL(input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();

    reader.onload = (e) => {
      $("#blah").attr("src", e.target.result).width(auto).height(auto);
    };

    reader.readAsDataURL(input.files[0]);
  }
}
