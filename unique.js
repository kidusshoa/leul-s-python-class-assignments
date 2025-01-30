let nums = [1, 2, 3, 3, 3, 3, 4, 5];
let nums2 = [];

for (let i = 0; i <= nums.length - 1; i++) {
  if (nums[i] != nums[i + 1]) {
    nums2.push(nums[i]);
  }
}

console.log(nums2);
