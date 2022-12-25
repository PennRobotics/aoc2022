#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <tgmath.h>

int digit_map(char c) {
  switch(c) {
    case '=':  return -2; break;
    case '-':  return -1; break;
    case '1':  return  1; break;
    case '2':  return  2; break;
    default:   return  0; break;
  }
}

char snafu_map(int d) {
  switch(d) {
    case -2:  return '='; break;
    case -1:  return '-'; break;
    case  1:  return '1'; break;
    case  2:  return '2'; break;
    default:  return '0'; break;
  }
}

struct divmod_s {
  int64_t quot;
  uint64_t rem;
};

struct divmod_s divmod(int64_t num, uint64_t den) {
  struct divmod_s result;
  printf("DIVMOD(%lld, %lld)", num, den);

  if (num < 0) {
    result.quot = (num-(den-1)) / den;
    result.rem = (num-(den-1)) % den + den - 1;
  } else {
    result.quot = num / den;
    result.rem = num % den;
  }

  printf(" = %lld, %lld\n", result.quot, result.rem);

  return result;
}

int main() {
  char *line;
  size_t len;
  //FILE *fh = fopen("sample25", "r");
  FILE *fh = fopen("input25", "r");
  int i;
  uint64_t sum = 0;

  while( getline(&line, &len, fh) != -1 ) {
    for(i = 0; i < len; ++i) {
      if (line[i] == '\n')  { line[i] = '\0'; break; }
    }
    for(int d=i-1, i=0; d >= 0; --d, ++i) {
      sum += (uint64_t)pow(5, i) * digit_map(line[d]);
    }
  }

  fclose(fh);

  int8_t *digs;
  int8_t pad = 2*i;
  struct divmod_s dm;
  int8_t dig;

  digs = (int8_t *)malloc(pad * sizeof(int8_t));
  memset(digs, 0, pad);

  i = 0;
  for(;;) {
    if (sum / (uint64_t)powl(5, ++i) == 0)  { break; }
  }

  printf("%d\n", i);

  for(int d=i-1; d >= 0; --d) {
    printf("%d . ", d);
    dm = divmod(sum, (uint64_t)pow(5, d));
    printf("%lld  %lld\n", dm.quot, dm.rem);
    dig = dm.quot;
    sum = dm.rem;
    digs[d] += dig;
    for (int scan=d; scan<i; ++scan) {
      printf(".");
      if (digs[scan] > 2) {
        digs[scan] -= 5;
        digs[scan+1] += 1;
      }
    }
  }

  for(int a=5; a<7; a++)  { 0; }  // TODO-debug: adding this line causes segfault
  //for(int s=0; s<10; s++) {}
    //printf("%lld\n", (uint64_t)digs); // TODO-debug
    //printf("%d: %d\n", s, *(digs+s));
//  }
  //printf("\n");

  // free(digs);

  printf("Part A: %lld\n", 0);
  printf("Part B: %lld\n", 0);
}
