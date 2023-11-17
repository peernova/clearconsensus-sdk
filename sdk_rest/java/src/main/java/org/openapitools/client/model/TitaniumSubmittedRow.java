/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumSubmittedRow
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:36:13.498051Z[UTC]")
public class TitaniumSubmittedRow {
  public static final String SERIALIZED_NAME_BENCHMARK = "benchmark";
  @SerializedName(SERIALIZED_NAME_BENCHMARK)
  private String benchmark;

  public static final String SERIALIZED_NAME_OUTLIER = "outlier";
  @SerializedName(SERIALIZED_NAME_OUTLIER)
  private String outlier;

  public static final String SERIALIZED_NAME_VALIDATION_ERROR_COUNT = "validationErrorCount";
  @SerializedName(SERIALIZED_NAME_VALIDATION_ERROR_COUNT)
  private Integer validationErrorCount;

  public static final String SERIALIZED_NAME_VALUES = "values";
  @SerializedName(SERIALIZED_NAME_VALUES)
  private List<Object> values = null;

  public TitaniumSubmittedRow() { 
  }

  public TitaniumSubmittedRow benchmark(String benchmark) {
    
    this.benchmark = benchmark;
    return this;
  }

   /**
   * Get benchmark
   * @return benchmark
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getBenchmark() {
    return benchmark;
  }


  public void setBenchmark(String benchmark) {
    this.benchmark = benchmark;
  }


  public TitaniumSubmittedRow outlier(String outlier) {
    
    this.outlier = outlier;
    return this;
  }

   /**
   * Get outlier
   * @return outlier
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOutlier() {
    return outlier;
  }


  public void setOutlier(String outlier) {
    this.outlier = outlier;
  }


  public TitaniumSubmittedRow validationErrorCount(Integer validationErrorCount) {
    
    this.validationErrorCount = validationErrorCount;
    return this;
  }

   /**
   * Get validationErrorCount
   * @return validationErrorCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getValidationErrorCount() {
    return validationErrorCount;
  }


  public void setValidationErrorCount(Integer validationErrorCount) {
    this.validationErrorCount = validationErrorCount;
  }


  public TitaniumSubmittedRow values(List<Object> values) {
    
    this.values = values;
    return this;
  }

  public TitaniumSubmittedRow addValuesItem(Object valuesItem) {
    if (this.values == null) {
      this.values = new ArrayList<>();
    }
    this.values.add(valuesItem);
    return this;
  }

   /**
   * Get values
   * @return values
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<Object> getValues() {
    return values;
  }


  public void setValues(List<Object> values) {
    this.values = values;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumSubmittedRow titaniumSubmittedRow = (TitaniumSubmittedRow) o;
    return Objects.equals(this.benchmark, titaniumSubmittedRow.benchmark) &&
        Objects.equals(this.outlier, titaniumSubmittedRow.outlier) &&
        Objects.equals(this.validationErrorCount, titaniumSubmittedRow.validationErrorCount) &&
        Objects.equals(this.values, titaniumSubmittedRow.values);
  }

  @Override
  public int hashCode() {
    return Objects.hash(benchmark, outlier, validationErrorCount, values);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumSubmittedRow {\n");
    sb.append("    benchmark: ").append(toIndentedString(benchmark)).append("\n");
    sb.append("    outlier: ").append(toIndentedString(outlier)).append("\n");
    sb.append("    validationErrorCount: ").append(toIndentedString(validationErrorCount)).append("\n");
    sb.append("    values: ").append(toIndentedString(values)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("benchmark");
    openapiFields.add("outlier");
    openapiFields.add("validationErrorCount");
    openapiFields.add("values");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumSubmittedRow
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumSubmittedRow.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumSubmittedRow is not found in the empty JSON string", TitaniumSubmittedRow.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumSubmittedRow.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumSubmittedRow` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("benchmark") != null && !jsonObj.get("benchmark").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `benchmark` to be a primitive type in the JSON string but got `%s`", jsonObj.get("benchmark").toString()));
      }
      if (jsonObj.get("outlier") != null && !jsonObj.get("outlier").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `outlier` to be a primitive type in the JSON string but got `%s`", jsonObj.get("outlier").toString()));
      }
      // ensure the json data is an array
      if (jsonObj.get("values") != null && !jsonObj.get("values").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `values` to be an array in the JSON string but got `%s`", jsonObj.get("values").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumSubmittedRow.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumSubmittedRow' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumSubmittedRow> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumSubmittedRow.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumSubmittedRow>() {
           @Override
           public void write(JsonWriter out, TitaniumSubmittedRow value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumSubmittedRow read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumSubmittedRow given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumSubmittedRow
  * @throws IOException if the JSON string is invalid with respect to TitaniumSubmittedRow
  */
  public static TitaniumSubmittedRow fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumSubmittedRow.class);
  }

 /**
  * Convert an instance of TitaniumSubmittedRow to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

